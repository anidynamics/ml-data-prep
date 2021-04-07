import os
import click
import pandas as pd


def create_dfs_from_folders(path_to_folders):
    print("Creating dataframes from folders in " + path_to_folders + " ...")
    df = pd.DataFrame()
    for folder in os.scandir(path_to_folders):        
        for image_file in os.scandir(folder):
            df = df.append({'filename': os.path.basename(image_file), 'image_path': os.path.abspath(image_file), 'label': os.path.basename(folder)}, ignore_index=True)
    print("done","\n")
    df.to_csv(os.path.join(path_to_folders, 'df.csv'))
    return


@click.command()
@click.help_option('--help', '-h')
@click.option('--path', '-p', type=click.Path(exists=True), help='Path to folders')
# @click.option('--out_dir', '-o', help='Output directory')
def create_dataframe(path):
    if path == None:
        print("No path given")
    else:
        create_dfs_from_folders(path)

if __name__ == "__main__":
    create_dataframe()
