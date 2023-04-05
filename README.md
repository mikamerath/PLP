# PLP

**In Progress.** This will be the repository for the code for *Towards a Learning-Based Account of Local Phonological Processes* 

The code is already here, and I will be rolling out documentation on setting it up, running it, and extending it to your own data. Stay tuned!  

```bibtex
@article{belth2022locality,
  title={A Learning-Based Account of Local Phonological Processes},
  author={Belth, Caleb},
  journal={Phonology},
  note={In Press},
  year={2023},
  publisher={Cambridge University Press}
}
```

## Usage Examples

All examples assume that you are running from the ```src/``` directory. If this is not the case, you can add the ```src/``` directory to the current path, as shown below, before importing the code.

```python
>> import sys
>> sys.path.append(path_to_src)
```

### Loading Data

Below is an example of how to load the German corpus.

```python
>> from utils import load
>> pairs, freqs = load('../data/german/ger.txt', skip_header=True)
```

### Running PLP

Here is an example of running PLP on the first 1K words from the German corpus. See above for loading (UR, SR) pairs.

```python
>> from plp import PLP
>> plp = PLP(ipa_file='../data/german/ipa.txt')
>> plp.train(pairs[:1000])
>> print(plp)
1: {+voi,-son} --> [-voi] /  __ .
```