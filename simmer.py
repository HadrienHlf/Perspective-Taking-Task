import os
import numpy as np
import json


def simmer():

    # LAYER 1: CREATING LINES
    with open('results.txt', 'r') as results_file:
        filedata = results_file.read()

    filedata = filedata.replace("},{", "\n\n\n\n")
    filedata = filedata.replace(',"', "\n")
    filedata = filedata.replace('"', "")

    results_file.close()

    with open('results.txt', 'w') as results_file:
        results_file.write(filedata)

    results_file.close()

    # LAYER 2: SUPPRESSING IRRELEVANT RANKS
    with open("results.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if (("null" not in line.strip("\n")) and ("stimulus" not in line.strip("\n"))) and (("internal_node" not in line.strip("\n")) and ("trial_type" not in line.strip("\n"))):
                    output.write(line)
    input.close()
    output.close()

    # replace file with original name
    os.replace('temp.txt', 'results.txt')

    # LAYER 3: SUPPRESSING IRRELEVANT TRIALS
    with open("results.txt", "r") as input:
        with open("temp.txt", "w") as output:
            paragraph_started = False
            interesting = False
            paragraph = []
            tot_count = 0
            for line in input:
                paragraph.append(line)
                if ("rt" in line.strip("\n")):
                    paragraph_started = True
                if ("trial_number" in line.strip("\n")):
                    interesting = True
                if ("emailid" in line.strip("\n")):
                    interesting = True
                if ("time_elapsed" in line.strip("\n")):
                    paragraph_started = False
                if ((not paragraph_started) and interesting):
                    tot_count += 1
                    for linearr in paragraph:
                        output.write(linearr)
                if (not paragraph_started):
                    paragraph.clear()
                    interesting = False

                if ("correct:" in line.strip("\n")):
                    output.write(line)
            output.write("Answers Processed: "+str(tot_count))
    input.close()
    output.close()

    # replace file with original name
    os.replace('temp.txt', 'results.txt')

    # LAYER 4: SUPPRESS ALL IRRELEVANT INFORMATION IN REMAINING TRIALS
    with open("results.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if (("rt:" not in line.strip("\n")) and ("response:" not in line.strip("\n"))) and (("time_elapsed:" not in line.strip("\n")) and ("trial_index:" not in line.strip("\n"))):
                    output.write(line)
                if ("emailid" in line.strip("\n")):
                    output.write(line)
                if ("rt:" in line.strip("\n")):
                    output.write("\n"+line)
    input.close()
    output.close()

    # replace file with original name
    os.replace('temp.txt', 'results.txt')
    
    tot_count=tot_count-1
    mat = [["0" for _ in range(4)] for _ in range(tot_count)]
    id_num = 0
    

    # LAYER 5: MATRIX
    with open("results.txt", "r") as input:
        # iterate all lines from file
        count = 0
        for line in input:
            # record the right information
            if ('emailid' in line):
                id_num = int(line.strip("\n")[8::])
                
            if ("rt:" in line):
                mat[count][0] = line.strip("\n")[3::]
            if ("task:" in line):
                mat[count][1] = line.strip("\n")[5::]
            if ("trial_number:" in line):
                mat[count][2] = line.strip("\n")[13::]
            if ("correct:" in line):
                mat[count][3] = line.strip("\n")[8::]
                count += 1

    trials_list = []
    for m in range(tot_count):
        trial = {"RT": int(mat[m][0]), "Type": mat[m][1],
                "Trial_id": mat[m][2], "is_correct": mat[m][3]}
        trials_list += [trial]


    # LAYER 6
    final_matrix = np.zeros((9, 3))
    evolution = np.zeros((3, 8))
    for i in range(tot_count-1):
        if i < tot_count-128:
            if int(mat[i][0]) < 3000:
                final_matrix[0][0] += 1
                final_matrix[0][1] += int(mat[i][0])
                if mat[i][3] == 'true':
                    final_matrix[0][2] += 1
        else:
            if int(mat[i][0]) < 3000:
                if int(mat[i][2]) in [0, 1, 2, 3, 4, 5, 6, 7]:
                    final_matrix[1][0] += 1
                    final_matrix[1][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[1][2] += 1

                if int(mat[i][2]) in [8, 9, 10, 11, 12, 13, 14, 15]:
                    final_matrix[2][0] += 1
                    final_matrix[2][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[2][2] += 1

                if int(mat[i][2]) in [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]:
                    final_matrix[3][0] += 1
                    final_matrix[3][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[3][2] += 1

                if int(mat[i][2]) in [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]:
                    final_matrix[4][0] += 1
                    final_matrix[4][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[4][2] += 1

                if int(mat[i][2]) in [40, 41, 42, 43, 44, 45, 46, 47]:
                    final_matrix[5][0] += 1
                    final_matrix[5][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[5][2] += 1

                if int(mat[i][2]) in [48, 49, 50, 51, 52, 53, 54, 55]:
                    final_matrix[6][0] += 1
                    final_matrix[6][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[6][2] += 1

                if int(mat[i][2]) in [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]:
                    final_matrix[7][0] += 1
                    final_matrix[7][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[7][2] += 1

                if int(mat[i][2]) in [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]:
                    final_matrix[8][0] += 1
                    final_matrix[8][1] += int(mat[i][0])
                    if mat[i][3] == 'true':
                        final_matrix[8][2] += 1
                eighth = int((i-(tot_count-128))/16)
                evolution[0][eighth] += int(mat[i][0])
                evolution[2][eighth] += 1
                if mat[i][3] == 'true':
                    evolution[1][eighth] += 1
    for j in range(9):
        final_matrix[j][1] = round(final_matrix[j][1]/float(final_matrix[j][0]), 2)
        final_matrix[j][2] = round(final_matrix[j][2]/float(final_matrix[j][0]), 2)

    for h in range(8):
        evolution[0][h] = round(evolution[0][h]/float(evolution[2][h]), 2)
        evolution[1][h] = round(evolution[1][h]/float(evolution[2][h]), 2)


    eight_conditions = []
    evolution_list = []
    listcond = ["Example Round", "True Consistent You Trials", "True Consistent Them Trials", "True Inconsistent You Trials", "True Inconsistent Them Trials",
                "False Consistent You Trials", "False Consistent Them Trials", "False Inconsistent You Trials", "False Inconsistent Them Trials"]

    # LAYER 7: WRITING RESULTS
    for i in range(9):
        recap = {'accepted': final_matrix[i][0],
                'rt': final_matrix[i][1], 'accuracy': final_matrix[i][2]}
        eight_conditions += [recap]
        recap_string = listcond[i].upper()+" — Trials accepted: "+str(final_matrix[i][0]) + \
            " Mean Reaction Time: " + \
            str(final_matrix[i][1])+" Accuracy: "+str(final_matrix[i][2])+"\n"
    for h in range(8):
        recap = {'accepted': evolution[2][h],
                'rt': evolution[0][h], 'accuracy': evolution[1][h]}
        evolution_list += [recap]
        recap_string = "BLOCK N°"+str(h)+" – Trials accepted: "+str(
            evolution[2][h])+" Mean Reaction Time: "+str(evolution[0][h])+" Accuracy: "+str(evolution[1][h])+"\n"

    zip_iterator = zip(listcond, eight_conditions)
    conditions = dict(zip_iterator)

    run = {'ID': id_num, 'raw': trials_list,
        'conditions': conditions, 'evolution': evolution_list}
    return run