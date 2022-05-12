# implementation

## structure

The program has commandline ui and huffman coding and Lempel-Ziv-welch implemented in their own files, and the binary tree for huffman implemented in it's own file.

## time and space complexity

Huffmans algorithm has time complexity of O(n log n), Lempel-Ziv-Welch has time complexity of O(n).

## comparison

In my im empirecal testing I have found that, with reasonably big files, both have compresson rates of 40%-50%, with Lempel–Ziv–Welch usually having couple extra prosents better rates.

## improvements

Currently when using huffmans algorithm it produces binary that contains how long the compressed data is and how long the huffman tree is, it would be possible to save couple of bits by saving lenght of compressed data and the amount of extra bits instead.

## sources

[huffman on wikipedia](https://fi.wikipedia.org/wiki/Huffmanin_koodaus)

[Lempel-Ziv on wikipedia](https://fi.wikipedia.org/wiki/Lempel-Ziv)
