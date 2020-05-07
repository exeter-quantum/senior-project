SRP\*400: Quantum computing senior project
==========================================

Insert description / abstract here.

by [Evan Chandran](https://github.com/ecchandran) and [Maxwell Wang](https://github.com/maxzwang)

**Advisor**: [Jim DiCarlo](https://www.exeter.edu/faculty/james-dicarlo)

**Mentor**: [Peter Karalekas](https://github.com/karalekas)

## Running the notebooks locally

First, you will need to install the repository's requirements:

```bash
pip install -r requirements.txt
```

Then, you'll need to have local [qvm][qvm] and [quilc][quilc] servers (these are installed
separately -- see their READMEs for more info) running in the background:

```bash
qvm -S
```

```bash
quilc -R
```

Finally, you can bring up the JupyterLab interface by doing the following:

```bash
jupyter lab
```

Which should automatically open a tab in your browser, allowing you to interact with the
GHZ and Deutsch-Josza notebooks.

## Docker configuration

The Docker image for this repo is built using the [`rigetti/forest-notebook`][forest-notebook] Docker
image, which comes with [pyQuil][pyquil] installed, [quilc][quilc] and [QVM][qvm] servers running
in the background, and additional Python packages for data analysis and visualization. To learn
more, check out the [rigetti/forest-notebook][forest-notebook-repo] repository.

[forest-notebook]: https://hub.docker.com/r/rigetti/forest-notebook
[forest-notebook-repo]: https://github.com/rigetti/forest-notebook
[pyquil]: https://github.com/rigetti/pyquil
[quilc]: https://github.com/rigetti/quilc
[qvm]: https://github.com/rigetti/qvm
