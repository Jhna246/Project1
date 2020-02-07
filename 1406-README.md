We want to implement a simple one-line editor. This editor is an editor that can only write lowercase English letters, up to 600,000 characters.

This editor has a cursor called 'cursor', which is placed at the beginning of the sentence (to the left of the first character), at the end of the sentence (to the right of the last character), or anywhere in the sentence (between any two consecutive characters). Can be located. That is, if a string of length L is currently entered in the editor, there are L + 1 places where the cursor can be placed.

The editor supports the following commands.

L Moves cursor one space to the left (ignored if cursor is at the beginning of a sentence)
D Moves cursor one space to the right (ignored if cursor is at end of sentence)
B Delete the character to the left of the cursor (ignored if the cursor is at the beginning of a sentence)
  The delete appears to move the cursor one space to the left, but the character that was actually to the right of the cursor remains the same
Add the character P $ $ to the left of the cursor
Given a string initially entered in the editor, followed by a sequence of commands entered, write a program to get the string entered in the editor after performing all commands. However, before the command is executed, the cursor is said to be at the end of the sentence.
