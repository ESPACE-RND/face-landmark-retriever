import ast

import pandas as pd


def load_excel(file_path):
    df = pd.read_excel(file_path)

    # Assuming 'landmarks' is the column containing the list of lists
    df[df.columns[1]] = df[df.columns[1]].apply(ast.literal_eval)

    # Now, you can create a representation for your targets
    targets = []

    for frame_landmarks in df[df.columns[1]]:
        for landmark in frame_landmarks:
            # Assuming 'x', 'y', 'z' are the properties for each landmark
            targets.append(float(landmark[0]))
            targets.append(float(landmark[1]))
            targets.append(float(landmark[2]))

    return targets
