# Project Name

## Installation

To run this project, you'll need to set up a Conda environment. Follow the steps below:

1. Make sure you have Conda installed. If not, you can download and install it from the official website: [https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Open a terminal or command prompt.
3. Create a new Conda environment named "yt_downloader" with Python 3.11 by running the following command:
   
   ```bash
   conda create -n yt_downloader python=3.11
   ```

4. Activate the newly created environment:

```bash
conda activate yt_downloader
```

5. To save the environment, run the following command:
   
   ```bash
   conda env export -n yt_downloader -f yt_downloader.yml
   ```
   
   This command exports the environment to a YAML file named "yt_downloader.yml".
6. You can now install any required dependencies and run the project within the "yt_downloader" environment.

