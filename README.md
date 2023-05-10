# Pencil Durability Kata
The purpose of the Pencil Durability Kata is to write code to simulate, first coarsely and then more faithfully, an ordinary graphite pencil. It includes writing and editing text, point degradation, using the eraser, and sharpening the pencil. The point of this kata is to provide a larger-than-trivial exercise that can be used to practice TDD. A significant portion of the effort will be in determining which tests should be written and, more importantly, written next.

## Write
> **AS A** writer,  
**I WANT** to be able to use a pencil to write text on a sheet of paper  
**SO THAT** I can better remember my thoughts.  

When the pencil is instructed to write a string of text on a sheet of paper, the paper should reflect the text that was written.

Text written by the pencil should always be appended to existing text on the paper. Thus, given a piece of paper with the text "She sells sea shells", when a pencil is instructed to write "&nbsp;down by the sea shore" on the paper, the paper will then contain the entire string (i.e. "She sells sea shells down by the sea shore").


## Erase
> **AS A** writer,  
**I WANT** to be able to erase previously written text  
**SO THAT** I can remove my mistakes.  

When the pencil is instructed to erase text from the paper, the last occurrence of that text on the paper will be replaced with empty spaces.  

Given a piece of the paper containing the string:  
	"How much wood would a woodchuck chuck if a woodchuck could chuck wood?"  
when the string "chuck" is erased, the paper should read:  
	"How much wood would a woodchuck chuck if a woodchuck could&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wood?"    
and if the string "chuck" is erased again, the paper should read:  
"How much wood would a woodchuck chuck if a wood&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;could&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wood?"  
