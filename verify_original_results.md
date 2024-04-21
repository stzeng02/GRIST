Original experiment used:
Our experiment was conducted on the Intel Xeon Silver 4214 machine with 128GB RAM,
Ubuntu 16.04.6 LTS, and two GTX 2080 Ti GPUs.

My PC settings:
Processor	13th Gen Intel(R) Core(TM) i9-13900KF, 3000 Mhz, 24 Core(s), 32 Logical Processor(s)
Installed Physical Memory (RAM)	32.0 GB
Adapter Description	NVIDIA GeForce RTX 4070 (VRAM 16GB GDDR6X)

Bug IDs which use MNIST:

14:

Expected Average:
86.23 seconds over 10 runs

Testing:

INFO: Iter: 882 Current Time cost:0:00:13.408662 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #MNIST_grist# Success to find NaN!  Iteration: <882> Time cost: <0:00:13.408662>.

IndexError: index 0 is out of bounds for axis 0 with size 0

IndexError: index 0 is out of bounds for axis 0 with size 0

IndexError: index 0 is out of bounds for axis 0 with size 0

IndexError: index 0 is out of bounds for axis 0 with size 0

IndexError: index 0 is out of bounds for axis 0 with size 0

21:

Expected Average:
44.49 seconds over 10 runs

Testing:

Observed Average:

25:

Expected Average:
59.36 seconds over 10 runs

Testing:
INFO: Iter: 8800 Current Time cost:0:00:19.857463 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.857463>.

INFO: Iter: 8800 Current Time cost:0:00:19.539521 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.539521>.

INFO: Iter: 8800 Current Time cost:0:00:19.982860 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.982860>.

INFO: Iter: 8800 Current Time cost:0:00:19.812511 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.812511>.

INFO: Iter: 8800 Current Time cost:0:00:19.890835 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.890835>.

INFO: Iter: 8800 Current Time cost:0:00:19.439454 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.439454>.

INFO: Iter: 8800 Current Time cost:0:00:19.610097 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.610097>.

INFO: Iter: 8800 Current Time cost:0:00:19.795301 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.795301>.

INFO: Iter: 8800 Current Time cost:0:00:19.480155 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.480155>.

INFO: Iter: 8800 Current Time cost:0:00:19.469738 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #tensorflow_mnist_grist# Success to find NaN!  Iteration: <8800> Time cost: <0:00:19.469738>.

Observed Average:
19.6877935 over 10 runs

31:

Expected Average:
23.79 over 3 runs (only 3 out of 10 succeed)

Testing:

INFO: Iter: 1100 Current Time cost:0:00:39.330072 Loss: 0.39636582136154175 Object function value: 1.0355935664563276e-08 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:36.092593 Loss: 0.18719618022441864 Object function value: 0.0006535918801091611 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 469 Current Time cost:0:00:16.548005 Loss: inf Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #GAN_MNIST_grist# Success to find NaN!  Iteration: <469> Time cost: <0:00:16.548005>.

INFO: Iter: 183 Current Time cost:0:00:06.171514 Loss: nan Object function value: inf Change step: 0.15
FINAL RESULTS: #GAN_MNIST_grist# Success to find NaN!  Iteration: <183> Time cost: <0:00:06.171514>.

INFO: Iter: 1100 Current Time cost:0:00:37.656667 Loss: 0.3264138400554657 Object function value: 3.324961486694811e-11 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:36.149891 Loss: 0.17482437193393707 Object function value: 0.009014297276735306 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:36.573532 Loss: 0.2023785263299942 Object function value: 0.2703247368335724 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:37.526819 Loss: 0.1863834410905838 Object function value: 0.0004292108933441341 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:37.036162 Loss: 0.13248296082019806 Object function value: 0.036791909486055374 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

INFO: Iter: 1100 Current Time cost:0:00:36.877584 Loss: 0.13502417504787445 Object function value: 0.004988701082766056 Change step: 0.15
IndexError: index 0 is out of bounds for axis 0 with size 0

Observed Average:
11.3597595 over 2 Runs (2/10 succeed)