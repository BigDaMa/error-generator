import numpy as np
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.neighbors import KNeighborsClassifier

# find the most important feature and try to change the target only by changing this feature.
class Change_Most_Important_Feature(object):
    def __init__(self):
        pass

    def change(self,x_train, y_train, percetage, mnb, change_plan):
        number_change_requested = int(percetage / 100 * x_train.shape[0])
        print("{} percentage error is equal to {} change \n".format(percetage, number_change_requested))

        #find the most important feature

        sfs1 = SFS(mnb,
                   forward=True,
                   floating=False,
                   verbose=2,
                   scoring='accuracy',
                   cv=0)

        sfs1 = sfs1.fit(x_train, y_train)
        print("the most important feature is column {}".format(sfs1.k_feature_idx_[0]))
        feature=sfs1.k_feature_idx_[0]
        used_row = []
        col_history = []
        occurred_change = 0
        all_changed = 1
        x_train_changed = np.copy(x_train)

        for i in range(len(change_plan["number"])):
            occurred_change = 0

            indices = [t for t, x in enumerate(y_train) if x == change_plan["key"][i][0]]
            # print(indices)
            for p in range(len(indices)):
                if y_train[indices[p]] == mnb.predict([x_train[indices[p]]]):

                    x_train_changed[indices[p]][feature] = 0

                    if (change_plan["key"][i][1] == mnb.predict([x_train_changed[indices[p]]])[0]):

                        print(x_train[indices[p]], mnb.predict([x_train[indices[p]]])[0])
                        print(x_train_changed[indices[p]], mnb.predict([x_train_changed[indices[p]]])[0])
                        print(" \n change number {} \n".format(all_changed))

                        occurred_change = occurred_change + 1
                        all_changed = all_changed + 1
                        col_history = []
                        break

                    else:
                        x_train_changed[indices[p]] = np.copy(x_train[indices[p]])

        if (all_changed < number_change_requested - 1):
            print("your request doesn't complete! please change your plan")
        return np.copy(x_train_changed)
