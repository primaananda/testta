import itertools
from synsets_extraction import synsets_extraction

x1 = ['ahad', 'esa', 'satu', 'tunggal']
x2 = ['ahad', 'minggu']

def calculate_distance(synset1, synset2):
    similar_word = 0
    sum_word = len(synset1) + len(synset2)
    for word1 in synset1:
        for word2 in synset2:
            if word1 == word2:
                similar_word += 1
                sum_word -= 1
    return similar_word/sum_word

def complete_link(cluster1, cluster2):
    max_distance = None
    for point_a in cluster1:
        for point_b in cluster2:
            dist = calculate_distance(point_a, point_b)
            if max_distance is None:
                max_distance = dist
            else:
                if dist > max_distance:
                    max_distance = dist
    return max_distance

def agglomerative_clustering(dataset):
    current_cluster = dataset
    output_cluster = []
    alpha = 0.5
    cluster1 = []
    cluster2 = []
    for data in current_cluster:
        cluster1 = data
    for data2 in current_cluster:
        cluster2 = data2
    dist = complete_link(cluster1, cluster2)
    print(dist)
        # if np.array(cluster1).shape == (2,):
        #     cluster1 = [cluster1]
        # if np.array(cluster2).shape == (2,):
        #     cluster2 = [cluster2]
        #
        # dist = complete_link(cluster1, cluster2)
        # if dist >= alpha:
        #     aa

file1 = open('datatest/1.json')
synsets = synsets_extraction(file1)
agglomerative_clustering(synsets)
hasil = calculate_distance(x2,x1)
#print(hasil)