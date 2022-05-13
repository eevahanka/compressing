# implementation
## structure
The program has commandline ui and Huffman coding and Lempel-Ziv-Welch implemented in their own files, and the binary tree for Huffman implemented in it's own file.
## time and space complexity
Huffman algorithm has time complexity of O(n log n), Lempel-Ziv-Welch has time complexity of O(n).
## comparison
In my empirical testing I have found that, with reasonably big files, both have compression rates of 40%-50%, with Lempel-Ziv-Welch usually having couple extra prosents better rates.
## improvements
Currently when using Huffman algorithm it produces binary that contains how long the compressed data is and how long the Huffman tree is, it would be possible to save couple of bits by saving length of compressed data and the amount of extra bits instead.
## sources


[huffman on wikipedia](https://fi.wikipedia.org/wiki/Huffmanin_koodaus)

[Lempel-Ziv on wikipedia](https://fi.wikipedia.org/wiki/Lempel-Ziv)
