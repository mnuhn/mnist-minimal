# Minimal example of parsing and displaying MNIST data

## Instructions
1. Run `bash download_mnist.sh` to download the dataset.
2. Run `python3 display_mnist.py` to display the data.

## Explanation
A simple mapping from the image data bytes to ASCII is used to display the
images on the terminal: 

ASCII | ` ` | ``` | `.` | `:` | `^` | `~` | `;` | `+` | `*` | `?` | `D` | `0` | `#` | `%` | `B` | `@`
-----:|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----
From  |   0 |  16 |  32 |  48 |  64 |  80 |  96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |
To    |  15 |  31 |  47 |  63 |  79 |  95 | 111 | 127 | 143 | 159 | 175 | 191 | 207 | 223 | 239 | 255 |

## Example output
```
Entry: #0084, Label: 8
==========================================================
=                                                        =
=                                                        =
=                                                        =
=                                                        =
=                                                        =
=                                  ^   ; 0 0 ~ `         =
=                            ; # B ~   % @ @ @ +         =
=                    ` : ; # @ 0 `     ~ @ @ @ ~         =
=                ` ~ B @ @ % ~       + @ @ 0 :           =
=                * @ @ % +       : # @ @ *               =
=              ; @ @ % .       : @ @ % `                 =
=            . @ @ % :       ` @ @ % `                   =
=            ~ @ @ :       ` # @ % `                     =
=            ` % @ B ? . . # @ #                         =
=              + @ @ @ @ B @ % `                         =
=                . ~ D @ @ @ @ # +                       =
=                      B @ B D B @ % ~                   =
=                    ; @ @ ;     . B @ *                 =
=                    ^ @ B           D @ :               =
=                    ; @ @ `         ~ @ #               =
=                    ~ @ @ `         * @ +               =
=                      % @ ^         0 @ :               =
=                      ^ @ % `     + @ 0                 =
=                        ~ B % + 0 @ % `                 =
=                          ` ? # # ; `                   =
=                                                        =
=                                                        =
=                                                        =
==========================================================
```
