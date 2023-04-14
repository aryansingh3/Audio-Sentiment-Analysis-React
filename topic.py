def separate_by_class(dataset):
 separated = dict()
 for i in range(len(dataset)):
 vector = dataset[i]
 class_value = vector[-1]
 if (class_value not in separated):
 separated[class_value] = list()
 separated[class_value].append(vector)
 return separated
