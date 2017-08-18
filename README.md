This readme will be very brief

### Info
`Respair Interactions` is primarily a tool for verifying the integrity of MCCE output data. Essentially, the respair.lst file contains information on the interaction energis of all the hundreds of amino acids (the `respair.lst` file in this repo itself has over 21 thousand lines!). If an amino acid shares an abnormal amount of interaction energy with any other (abnormal is decided by the user, via the threshold), the program will return the details of the other amino acid(s) and the data associated with them.

### Usage

```
usage: main.py [-h] -a AMINO_ACID -t THRESHOLD

Checks for interaction energies that are very high (threshold indicated by
user)

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  -a AMINO_ACID, --amino_acid AMINO_ACID
                        Name of amino acid to be analyzed
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold determining whether an interaction energy is
                        erroneous or not
```

### Example

If you set a low threshold, it may return some anomalous amino acids.

```
python main.py -a ARG+A0002_ -t 0.1 
```
Returns...
```
------------------------------------------------------
THE FOLLOWING AMINO ACIDS CONTRIBUTED AN INTERACTION
ENERGY VIOLATING THE THRESHOLD (0.1)

              Partner    VDW  Elect Pairwise Charge  Interaction
Res
ARG+A0002_  ARGA0007_  -0.00   0.14     0.14   0.61         0.28
ARG+A0002_  ARGA0010_  -0.00   0.12     0.12   0.79         0.24
ARG+A0002_  ASPA0083_   0.00  -0.18    -0.18  -1.00         0.36
ARG+A0002_  LYSA0086_   0.00   0.19     0.19   1.00         0.38

THE TOTAL INTERACTION ENERGY WAS 2.27
------------------------------------------------------
```

If you set a higher threshold, it may return nothing at all. 
```
python main.py -a ARG+A0002_ -t 0.3
```
Returns...
```
------------------------------------------------------
THERE ARE NO AMINO ACID PARTNERS THAT CAUSE AN INTERA-
CTION ENERGY GREATER OR EQUAL TO THE PERCENTAGE THRES-
HOLD. (0.3)
THE TOTAL INTERACTION ENERGY WAS 2.27
------------------------------------------------------
```

