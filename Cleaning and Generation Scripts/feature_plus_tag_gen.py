import pandas as pd
import random


def create_tags(filename, start_index, stop_index):
    df = pd.read_csv(filename)
    num_rows = df.shape[0]
    index = []
    output = []
    random.seed(1)
    for i in range(1,num_rows+1):
        rand_feature = (random.randint(start_index, stop_index))
        output.append(rand_feature)
        index.append(i)
    df = pd.DataFrame(list(zip(index, output)), columns=['table_id', 'feature_id'])
    filename= filename.split('.csv')[0]
    df.to_csv(filename+"_tag.csv", header=True , index=False)
def create_features(list_of_lists):
    output = []
    for list in list_of_lists:
        for feature in list:
            output.append(feature)
    df = pd.DataFrame(output, columns=['feature_name'])
    df.to_csv("feature.csv", index=False)



def main():
    dining_features = ['drinks', 'healthy', 'outdoor', 'cafe', 'fast food', 'fine dining', 'late night', 'breakfast']
    entertainment_features = ['movies', 'music', 'live shows', 'comedy', 'sports']
    landmark_features = ['historical', 'natural', 'good view', 'guided tour']
    museum_features = ['art', 'science', 'music', 'interactive']
    park_features = ['park', 'beach', 'monument', 'garden']

    create_features([dining_features,entertainment_features,landmark_features,museum_features,park_features])

    create_tags('dining_clean.csv',1,8)
    create_tags('entertainment_clean.csv', 9,13)
    create_tags('landmark_clean.csv', 14,17)
    create_tags('museum_clean.csv', 18, 21)
    create_tags('park_clean.csv', 22,25)

main()