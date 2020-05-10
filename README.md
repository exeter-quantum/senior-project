SRP\*400: Quantum computing senior project
==========================================

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/exeter-quantum/senior-project/master?urlpath=lab/tree/Welcome.ipynb)

by [Evan Chandran](https://github.com/ecchandran) and [Maxwell Wang](https://github.com/maxzwang)

This winter ('20) at Phillips Exeter Academy we worked on a senior project in quantum computing, seeking to learn some of the theory and implications of quantum computation as well as run code on a real quantum computer. We began by studying quantum bits, gates, and circuits using David McMahon’s text *Quantum Computing Explained* \[1\]. To practice manipulating quantum bits, we used the Python quantum programming library [pyQuil](https://github.com/rigetti/pyquil) and the [Quantum Virtual Machine (QVM)](https://github.com/rigetti/qvm), a quantum simulator developed at [Rigetti Computing](https://rigetti.com) \[2\]. We simulated several quantum states such as the [Greenberger–Horne–Zeilinger (GHZ)](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state) \[3\] state, a generalized version of a simple entangled state. We also investigated the [Deutsch-Josza algorithm](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm) \[4\], one of the first algorithms created to demonstrate quantum advantage over a classical computer. In the last several weeks of our project, we used Rigetti’s Quantum Cloud Services (QCS) platform \[5\] to run code on a real Quantum Processing Unit (QPU), and documented our results.

**Advisor**: [Jim DiCarlo](https://www.exeter.edu/faculty/james-dicarlo)

**Mentor**: [Peter Karalekas](https://github.com/karalekas)

## Running the notebooks on Binder

This is a Binder repository, meaning that the Jupyter notebooks in this repository can be run online in a preconfigured execution environment, without any need for local setup. To run the notebooks online, click the "binder" badge above or the link [here](https://mybinder.org/v2/gh/exeter-quantum/senior-project/master?urlpath=lab/tree/Welcome.ipynb), and after a few moments a Jupyter Lab interface will launch. You will then be able to run the GHZ and Deutsch-Josza notebooks from your browser via a quantum simulator running in the background!

## Running the notebooks locally

If you would instead like to download the repository and run the notebooks on your own machine, you will first need to install the repository's requirements:

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

## References

1. McMahon, David. Quantum Computing Explained. John Wiley & Sons, 2007.
2. Robert S. Smith, Michael J. Curtis, and William J. Zeng. "A practical quantum instruction set architecture." [arXiv:1608.03355](https://arxiv.org/abs/1608.03355) (2016).
3. Daniel M. Greenberger, Michael A. Horne, and Anton Zeilinger. "Going Beyond Bell’s Theorem." [arXiv:0712.0921](https://arxiv.org/abs/0712.0921) (2017).
4. David Deutsch and Richard Jozsa. (1997) Rapid solution of problems by quantum computation. *Proc. R. Soc. Lond. A* **439**:553–558. http://doi.org/10.1098/rspa.1992.0167
5. Peter J Karalekas, Nikolas A Tezak, Eric C Peterson, Colm A Ryan, Marcus P da Silva, and Robert S Smith. A quantum-classical cloud platform optimized for variational hybrid algorithms. *Quantum Sci. Technol.* **5** 024003 (2020). http://dx.doi.org/10.1088/2058-9565/ab7559
