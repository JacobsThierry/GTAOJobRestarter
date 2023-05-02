

# GTA Online Job Restarter Script

This script is designed to automatically restart a job in GTA Online after it finishes. It will also prevent you from beeing auto-kicked because you're AFK. It is useful for jobs such as [my AFK survival](https://socialclub.rockstargames.com/job/gtav/tEjxk8ns9kSIl118o0jb-g).

## Requirements

- Python 3.x
- See `requirements.txt`

## Usage

1. Clone this repository to your local machine or [download the latest release](https://github.com/JacobsThierry/GTAOJobRestarter/releases/tag/v1.0.0).
2. Navigate to the directory containing the script in your command prompt/terminal.
3. Install the requirements by running `pip install requirements.txt`.
4. Start the script by running `python job_restarter.py`, start your AFK job and press `space`.
5. To stop the script, simply press `space` again.

## Troubleshooting

A few issues can occure when using this script.

### The script is trying to restart the job but does it too quickly

If you're facing this problem, you can replace the 0 in `time_offset = 0` at the begining of the file. This will slow down the restarting process by 2x the ammount you entered, in seconds.

### The script is not working for x job

The script is looking for pattern.png. However, some clouds pattern in certain jobs may prevent the script from recognizing the prompt. To prevent this from happening, you can take a new screenshot, crop it so it look like `pattern.png` and replace the said image.

## How It Works

The script takes a screenshot regulary and check if `pattern.png` is on screen. If so, it will start a serie of inputs to restart the job. Otherwise, it will press `ctrl` two times to prevent you from beeing kicked.

The script is also generating a log file so that you can monitor how long each job lasted.

## Disclaimer

This script is provided as-is and comes with no warranty or guarantee. Use at your own risk.

## Contributing

If you find any issues with the script, feel free to open an issue or submit a pull request.

## License

This script is under no license.