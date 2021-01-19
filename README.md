# titan-oscar

Scripts for installing and running TITAN on oscar.

## Getting Started

1. Clone this repository to the desired location on oscar (such as your data directory).

```
cd <directory where you want titan-oscar to live (e.g. ~/data/<your username>)>
git clone https://github.com/marshall-lab/titan-oscar.git
```

2. Make sure the pypy3 module is loaded

This can be done automatically by adding the following line to your `~/.modules` file so it is loaded whenever you log in to oscar, or you can run it only when desired.

```
module load pypy/7.3.0_3.6
```

3. Install the desired version of TITAN

> :warning: **Only works with TITAN versions 2.1.0 and higher**

This can either be the name of a [tag](https://github.com/marshall-lab/TITAN/releases) or a git commit hash (only recommended for developers).

This will always overwrite any existing version of titan you have installed.

```
./installTitan.py <version or hash>
./installTitan.py v2.1.0
./installTitan.py ab5df07247f315d676676fb83eb9ca3ec4a10b8b
```

This script will install titan as a package on pypy3, so you can `import titan` from pypy3 no matter where you are on oscar.

4. Submit a batch job for your run

To run titan on oscar, use the `subTitan.sh` script to submit a job.

Run `./subTitan.sh` for usage of the command.
