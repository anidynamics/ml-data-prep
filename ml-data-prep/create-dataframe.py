import click


# def create_dfs_from_folders(path_to_folders, manufacturer):
#     # Print some info
#     print("Creating dataframes from folders in " + path_to_folders + " ...")
#     list_of_dfs = []
#     for folder in os.scandir(path_to_folders):
#         df_model = pd.DataFrame()
#         for image_file in os.scandir(folder):
#             df_model = df_model.append({'filename': os.path.basename(image_file), 'image_path': os.path.abspath(image_file), 'manufacturer': manufacturer, 'model': os.path.basename(folder)}, ignore_index=True)
#         list_of_dfs.append(df_model)
#     print("done","\n")
#     return list_of_dfs


@click.command()
def create_dataframe():
    print("Works")


if __name__ == "__main__":
    create_dataframe()
