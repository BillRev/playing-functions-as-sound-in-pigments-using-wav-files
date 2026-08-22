# playing-functions-as-sound-in-pigments-using-wav-files
Python code which takes a function on an interval [a,b], and splits the function into n points, then represents each of the points as a sine wave so that the waves can be cycled through in Pigments, thus `playing' the function.
Each of the n sine waves is represented as a list of 2048 numbers between -1 and 1, and then the n lists are concatenated into one long list of n*2048 numbers. Then the code turns this list into a WAV file which can be imported into Pigments.
