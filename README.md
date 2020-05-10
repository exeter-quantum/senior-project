SRP\*400: Quantum computing senior project
==========================================

This winter ('20) at Phillips Exeter Academy we worked on a senior project in quantum computing, seeking to learn some of the theory and implications of quantum computation as well as run code on a real quantum computer. We began by studying quantum bits, gates, and tensor products using David McMahon’s text Quantum Computing Explained. To practice manipulating quantum bits, we used the Quantum Virtual Machine (QVM) and pyQuil, Rigetti’s Python library for quantum programming. We simulated several quantum states such as the Greenberger–Horne–Zeilinger (GHZ) state, a generalized version of a simple entangled state. We also investigated the Deutsch-Jozsa algorithm, one of the first algorithms created to demonstrate quantum advantage over a classical computer. In the last several weeks of our project, we used Rigetti’s Quantum Cloud Services (QCS) platform to run code on a real Quantum Processing Unit (QPU), and documented our results.

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

## References

McMahon, David. Quantum Computing Explained. John Wiley & Sons, 2007.

David Deutsch and Richard Jozsa. (1997) Rapid solution of problems by quantum computation. Proc. R. Soc. Lond. A 439:553–558. http://doi.org/10.1098/rspa.1992.0167

Daniel M. Greenberger, Michael A. Horne, and Anton Zeilinger. Going Beyond Bell’s Theorem, 2007. arXiv:0712.0921 [quant-ph]
