

# GTA Online Job Restarter Script

This script is designed to automatically restart a job in GTA Online after it finishes. It will also prevent you from beeing auto-kicked because you're AFK. It is useful for jobs such as [my AFK survival](https://socialclub.rockstargames.com/job/gtav/tEjxk8ns9kSIl118o0jb-g).

## Requirements

- Python 3.x
- See `requirements.txt`

## Usage

1. Clone this repository to your local machine or [download the latest release](https://github.com/JacobsThierry/GTAOJobRestarter/releases/tag/v1.0.1).
2. Navigate to the directory containing the script in your command prompt/terminal.
3. Install the requirements by running `pip install requirements.txt`.
4. Start the script by running `python job_restarter.py`, start your AFK job and press `space`.
5. To stop the script, simply press `space` again.

## Troubleshooting

A few issues can occure when using this script.

### The script is trying to restart the job but does it too quickly

If you're facing this problem, you can replace the 0 in `time_offset = 0` at the begining of the file. This will slow down the restarting process by 2x the ammount you entered, in seconds.

### The script is not working for x job

The script is looking for pattern.png. However, some clouds pattern in certain jobs may prevent the script from recognizing the prompt. To prevent this from happening, you can take a new screenshot, crop it so it look like `pattern.png` (you don't need to be very precise) and replace the said image.

### I don't have a qwerty keyboard

This script is assuming you're using a qwerty keyboard, with `w` as up and `s` as down. To change that, you can change `upButton = "w"` and `downButton = "s"` at the begining of the script.

### My game is not running at 1920x1080

Since the script is looking for an exact match of `pattern.png`, having the game running at a lower or higher resolution will not work. This can be worked arround by matching the image resolution and the game resolution

## How It Works

The script takes a screenshot regulary and check if `pattern.png` is on screen. If so, it will start a serie of inputs to restart the job. Otherwise, it will press `ctrl` two times to prevent you from beeing kicked.

The script is also generating a log file so that you can monitor how long each job lasted.

## Disclaimer

This script is provided as-is and comes with no warranty or guarantee. Use at your own risk.

## Contributing

If you find any issues with the script, feel free to open an issue or submit a pull request.

## License

This script is under no license.