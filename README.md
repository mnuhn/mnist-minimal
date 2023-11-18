# Minimal example of parsing and displaying MNIST data.

1. Run `bash download-mnist.sh` to download the dataset.
2. Run `python3 display-mnist.py` to display the data.

A simple mapping from the image data bytes to ASCII is used to display the
images on the terminal: Values "0-15" map to " ", 16-31 map to "\`", etc.

Example output:
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
