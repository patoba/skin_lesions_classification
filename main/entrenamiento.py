from modelo import RedNeuronal
import pytorch_lightning as pl
from pytorch_lightning import loggers as pl_loggers
from pytorch_lightning.callbacks.early_stopping import EarlyStopping

from preprocesamiento import train_data_loader, validation_data_loader, \
                             class_weights
from constantes import checkpoints_dir, logs_dir

tb_logger = pl_loggers.TensorBoardLogger(save_dir=logs_dir)

model = RedNeuronal(class_weights)
trainer = pl.Trainer(accelerator="gpu", precision = 16, 
                    default_root_dir = checkpoints_dir, 
                    callbacks = [EarlyStopping(monitor = "val_loss", mode = "min")],
                    logger = tb_logger)
trainer.fit(model, train_data_loader, validation_data_loader)
trainer.save_checkpoint(checkpoints_dir + "/final.ckpt")
