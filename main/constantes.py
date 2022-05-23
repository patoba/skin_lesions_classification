from pathlib import Path

main_dir = Path(__file__).parent / "../.."
main_dir = main_dir.resolve()
main_dir = str(main_dir)

data_dir = main_dir + "/datos/imagenes_train"
dest_dir = main_dir + "/datos/imagenes_train_mod"

test_size = 0.2
val_size = 0.2

norm_mean = (0.4914, 0.4822, 0.4465)
norm_std = (0.2023, 0.1994, 0.2010)

batch_size = 10
validation_batch_size = 10
shape = (224, 224)

checkpoints_dir = main_dir + "/checkpoints"
logs_dir = main_dir + "/logs"
