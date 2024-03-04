# PLTW Project 3.1.1 Combo Menu - using Data Classes
## Developer Notes
* Python version(s)
  * 3.10.11 (FiewalledReplit)
  * 3.12.2 (locally installed on my laptop)
  * Trying to sync between GitHub and GitLab
* Motivations
  * Use python data classes to separate out the following:
    * Menu Items - each item on the menu has a category, a name and a price.
    * Menu - consists of Menu Items and the ability to deliver a list of menu items for a given category
    * SingleOrder - a single customer order that knows how to ask questions about ordering 
      a menu item for a given category.
## References
* [Project 3.1.3](https://pltw.read.inkling.com/a/b/71ce293152cf4873b7395f3d59c64a57/p/667ce0d0f6bf463a8c2a3bcb4c2aa687)
## Requirements
The requirements are broken into multiple parts.
### Iteration 1
* Ask the user for a type of sandwich (chicken $5.25, beef $6.25, tofu $5.75).
* Have the program output the user’s sandwich selection to verify that the program is working correctly
### Iteration 2
Add the following features to your first iteration:

* Ask the user whether they would like a beverage (yes, no).
  *   If they say yes, ask what size beverage they would like:
      * small $1.00
      * medium $1.75
      * large $2.25
* Have the program output the user’s beverage size selection, or lack of selection, to verify that the program is working correctly.
* Have the program output the total cost so far.
### Iteration 3
Add the following features to your first iteration:

 * Ask the user whether they would like french fries (yes, no).
   * If they say yes, ask what size french fries they would like:
     * small $1.00
     * medium $1.50
     * large $2.00
   * If they say “small,” ask the user whether they’d like to mega-size their fries (yes, no). 
     * If the user inputs yes to mega-size, give them large fries at the large fries price instead of their small fries.
* Have the program output the user’s fries selection to verify that the program is working correctly.
* Adjust the program so the total cost only outputs to the user after their sandwich, drink, and fries selection.
### Iteration 4
* Ask the user how many ketchup packets they would like (enter a positive integer; cost is $0.25 per packet).

* After ordering the sandwich, drink, fries, and ketchup packets:
  * If the user selected a sandwich, french fries, and a beverage, reduce the total cost of the order by $1.00.
  * The program informs the user of their menu selections, for only the items they ordered. 
  * The program should print the total cost of the order. Remove any other totals before this point.
