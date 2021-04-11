import os
import click
import pandas as pd


def create_dfs_from_folders(path_to_folders, output_directory):
    # create a DataFrame from folders
    print("Creating dataframes from folders in " + path_to_folders + " ...")
    df = pd.DataFrame()
    for folder in os.scandir(path_to_folders):
        if os.path.isdir(folder):
            for image_file in os.scandir(folder):
                df = df.append({'filename': os.path.basename(image_file), 'image_path': os.path.abspath(image_file), 'label': os.path.basename(folder)}, ignore_index=True)
    print("Done.")

    # write DataFrame to csv file
    df_path = os.path.join(output_directory, 'df.csv')
    print("Wrinting dataframee to " + os.path.join(output_directory, 'df.csv') + " ...")
    df.to_csv(df_path)
    print("Done.")
    return


@click.command()
@click.help_option('--help', '-h')
@click.option('--path', '-p', type=click.Path(exists=True), help='Path to folders')
@click.option('--out_dir', '-o', help='Output directory of dataframe. Default: path to folders')
def create_dataframe(path, out_dir):
    if path == None:
        print("No path given")
        return
    else:
        if out_dir == "" or out_dir == None:
            out_dir = path
        create_dfs_from_folders(path, out_dir)


if __name__ == "__main__":
    create_dataframe()
