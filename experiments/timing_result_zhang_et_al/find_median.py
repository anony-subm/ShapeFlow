files = ["time_light_TF_GH_results_baseline2.txt"]
# files = ["time_Original_TF_SOF_results_baseline1.txt"]
light_files = ["time_light_TF_GH_results_baseline1.txt", "time_light_TF_GH_results_baseline2.txt", "time_light_TF_SOF_results_baseline1.txt","time_light_TF_SOF_results_baseline2.txt"]
original_files = ["time_Original_TF_GH_results_baseline1.txt","time_Original_TF_GH_results_baseline2.txt","time_Original_TF_SOF_results_baseline1.txt","time_Original_TF_SOF_results_baseline2.txt"]
# cleaning files
# file_name = "time_Original_TF_SOF_results_baseline2.txt"

# with open(file_name, "r") as f:
#     x = f.readlines()
#     # print(x)

# with open(file_name, "a") as f:
#     for l in x:
#         f.write(','.join(l.split()))
#         f.write('\n')

import pandas as pd

# for fl in files:
#     df = pd.read_csv(fl)
#     print(fl)
#     for c in df.columns:
#         print(round(df[c].median(), 6), c)
#     exit(0)

yes = []
for fl in light_files:
    df = pd.read_csv(fl)
    for c in df.columns:
        rel_std = df[c].var()*100/df[c].mean()
        # print(, df[c].mean(), c)
        if rel_std < 0.5:
            yes.append(True)
        # print(rel_std)
        else:
            print(rel_std, c, fl)
print(len(yes))
