# Testcase for reflex issue 4064

Steps to reproduce issue:

1. Install and run this reflex program
2. In the browser click the button labeled `Set public
variable to "hello" and private variable to "world"`
3. Notice that the public and private variable are set to "Hello" and "World" respectively
4. Press the "Reset State' button
5. Notice that the public variable is cleared but the private one is not.