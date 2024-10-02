import os
import zipfile
import multiprocessing

def unpack_zip(file):
    path_to_archives = r'../dataset/archives/'
    path_to_unpacked_chunks = r'../dataset/data/'
    
    try:
        with zipfile.ZipFile(os.path.join(path_to_archives, file), 'r') as zip_ref:
            zip_ref.extractall(path_to_unpacked_chunks)
        print(f"Unpacked: {file}")
    except Exception as e:
        print(f"Failed for: {file} with Error: {e}")

if __name__ == "__main__":
    path_to_archives = r'../dataset/archives/'

    # List all zip files in the directory
    zip_files = [file for file in os.listdir(path_to_archives) if file.endswith('.zip')]

    print(f"Start to unpack {len(zip_files)} files..")

    # Create a pool of workers
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()-2) as pool:
        pool.map(unpack_zip, zip_files)

    # Explicitly close the pool and wait for the worker processes to finish
    pool.close()  # Prevents any more tasks from being submitted to the pool
    pool.join()   # Waits for the worker processes to exit

    print("Finished unpacking archives.")
