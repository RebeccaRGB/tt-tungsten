![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Tungsten 8-Bit Elementary Cellular Automaton Processor

## How it works

Input the rule number / Wolfram code of an elementary cellular automaton on the
bidirectional pins and eight bits of the previous generation's state on the
dedicated input pins and the next generation's state will appear on the
dedicated output pins. The computation wraps around, so output 0 uses inputs
7, 0, and 1 as its previous state, and output 7 uses inputs 6, 7, and 0 as
its previous state.

## How to test

Set all bidirectional pins low (rule 0). All outputs should be low regardless of inputs.

Set all bidirectional pins high (rule 255). All outputs should be high regardless of inputs.

Set bidirectional pins 0, 1, 4, 5 low and 2, 3, 6, 7 high (rule 204). Each output should mirror its corresponding input.

Set bidirectional pins 0, 1, 4, 5 high and 2, 3, 6, 7 low (rule 51). Each output should invert its corresponding input.

You can find additional test cases in `test.py`.

## External hardware

Whatever switches or display elements or microcontrollers you want.

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)
