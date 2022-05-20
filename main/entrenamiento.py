import torch

from modelo import optimizer, net, criterion

from preprocesamiento import train_data_loader

num_epochs = 10
accuracy = []
val_accuracy = []
losses = []
val_losses = []

for epoch in range(num_epochs):
    running_loss = 0.0
    correct_total= 0.0
    num_samples_total=0.0
    for i, data in enumerate(train_data_loader):
        # get the inputs
        inputs, labels = data
        inputs, labels = inputs.to("cuda"), labels.to("cuda")
        # set the parameter gradients to zero
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        #compute accuracy
        _, predicted = torch.max(outputs, 1)
        corr = sum(predicted == labels).item() / len(labels)
        num_samples_total +=len(labels)
        correct_total +=corr
        running_loss += loss.item()

    running_loss /= len(train_data_loader)
    train_accuracy = correct_total/num_samples_total

    # val_loss, val_acc = evaluate(net, validation_data_loader)
    
    print('Epoch: %d' %(epoch+1))
    print('Loss: %.3f  Accuracy:%.3f' %(running_loss, train_accuracy))
    # print('Validation Loss: %.3f  Val Accuracy: %.3f' %(val_loss, val_acc))

    losses.append(running_loss)
    # val_losses.append(val_loss)
    accuracy.append(train_accuracy)
    # val_accuracy.append(val_acc)
print('Finished Training')


