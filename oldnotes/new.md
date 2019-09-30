# notes
## 7/1/2019


motivation: it feels like there should be a simple, generalized description of what i'm trying to accomplish.

the collapse is only ever determined just-in-time, but it collapses in such a way that consistency is maintained (never contradicts self) and certain things are conserved.
at the same time, collapse proceeds in a motivated way, to advance the general game state toward certain story goals.
this is the basis of the notion for the game. 
everything should be in superposition until just-in-time, when the scene is rendered for the player. 

observation happens when something must be rendered: the scene is observed (all objects visible in scene, not inside or behind other objects)

## Statement of problem

the plot proceeds according to high-level directives:

* player learns of kidnapping
    1. information discovery
* player confronts bad guy 
    1. bad guy discovery
    2. bad guy battle
* player learns secret location
    1. information discovery
* player confronts boss in secret location
    1. player in location
    2. bad guy battle
* player frees the kidnapped person
    1. information discovery
    2. player in location


identify the current imperative:

``` 
information discovery
        type: bad guy plot 
        contenet: {person} is kidnapped
```

imperative must be made concrete:

    "tell the player that {bad guy} has kidnapped {person}"

the specifics are provided by script, the imperative is 
more general (applies to more than just this script, connects up with system)
so, plot configuration is instruction for an imperative factory.

## imperatives

* in terms of a state satisfaction:
  * state.information.contains(plot[232423])
  * "when state is achieved"
  * possibly complicated
* update its state when it triggers 
  * not as flexible, does not recognize if satisfied by different means
* **or it might be phrased as a callback of a certain action:**
  * when(information displayed)
  * only difficulty: specifying which information
  * "when action occurs"

then we have the state, and possibilities.
possibilities are:
1. object in superposition exposes superposed callbacks
2. existing objects expose action callbacks
   
among those possibilities are ways we can satisfy the imperative:
1. open a drawer, find a note: the note yields information
2. phone rings, answer it, a voice says information
3. a brick is thrown through window. tied to brick is note. note yields information.

if we wanted to phrase this in terms of projections, it would have to look like:

$$<I | A> \rightarrow \{ phone, window, note \}$$

## Motivated Collapse
when the player opens the drawer, any object might be in there:

```
item: {book, gun, knife, candle, ticket stub, matchbook, note}
```

so we have a state, a player action which triggers an observation of inside of drawer. 
now we have a state, a collapse, and an imperative.

the goal is for collapser to realize that if we collapse to note, note can contain the required information, and the player reading that achieves the desired state. 

the outcome of the motivated collapse should be to choose the note, then: $\widehat{O}\ i \rightarrow note$.
how does the collapser differentiate the note vs. the candle, e.g.?

looking at it at the object level is probably a mistake: 
*how would this look in nonmotivated collapse?
note could be a ransom note in that case, if fully general?
if not full general, how does note.text accept a ransom note?*

instead the collapser needs to consider what action interfaces the superposition exposes. 

maybe the player doesn't read the note, but we can allow that placing the note is sufficient via recursion:
when reading the note, motivated collapse will make it a ransom note.
we can't force the player's hand, but we can choose the situation that makes imperative more likely.

#### unknown but solvable: deciding that y is closer to imperative goal than x

## collapse vs. action:

look more closely at the "motivated collapse" of the note text.
How do we link the exposed action interface perspective with the quantum state perspective?

1. reading the note should collapse note.text and information provided should just be note.text.
2. reading the note should short-circuit the note.text state and override it with text provided by imperative.

choice 2 is pointing in a new direction: functional recasting of superposition and collapse.
there are two behaviors, depending on whether we are motivated or not. 
this suggests that context free grammar could be just a special case of the overarching system.

**Functional aspect**

* exposed action interfaces that specify types of transformations on state allow the determination of imperative distance and motivated collapse.

**Superposition aspect**

* certain functions may only work if the player has not observed an outcome yet. if a player has observed a outcome, the future is consistent with that. some actions are only exposed by superpositions.

## functional specification

environments and objects expose state-mutating functions with the signature:

$$
f: imperative \rightarrow s'
$$

e.g. a window exposes several possible state actions:

* imperative: supply information from the bad guys
  * a note tied to a brick gets tossed through window
* allow a character to enter
  * character enters through the window
* allow player to spot something
  * player sees the event through the window

because these actions are specified as functions that take imperative in their signature, the specifics can be generated / inferred in a way that is guaranteed to be consistent.

generality can be attained by subclassing imperatives: e.g. the imperative that player learns of kidnapping is a kind of information transfer. thus any exposed action that can satisfy an information transfer can satisfy the imperative.

i suspect that we want to avoid generalization: generalization tends to break things which need to be specific. e.g.:

television can provide general information transfer. note can achieve general information transfer. but the way they achieve ransom notice is different:

* tv: news story about kidnapping
* note: ransom note from kidnapper

## generalizing functional approach

we have imperative: player learns information from bad guys. 
we want to enumarate the ways this imperative can be satisfied by the environment. 
we find:

1. (window) brick gets tossed through window
2. (telephone) player gets a phone call
3. (letter) player opens a letter received in the mail

#### static methods
any number of different bricks may be tossed through the window at any time, and any number of phone calls may be received, without ever compromising internal consistency.
these actions are exposed intrinsically by the object.

#### wavefunction collapse
if the player has opened the letter and read it before this directive, it is already collapsed and can't contain new information.
therefore, it is not intrinsic to the letter object, but to its superposition.

if it is not collapsed, the player may interact with (read) it, at which time it will satisfy the imperative and its contents will be the requisite bad guy information.
at any future time, if the player reads the letter again, it will contain the bad guy information: it is no longer a superposition.

overall, this is different in that it requires player interaction, and it is sourced by superpositions, not the object itself.

the hope is that both actions can share a parent class.

## wavefunction collapse

the concrete object, letter, has no static actions.
a superposition of letter exposes static actions.
somehow, creating a superposition of concrete objects creates new actions from the potential of collapsing a wavefunction.

$$
l: L
\\
\Psi: \{l\}
\\
\Psi.f : i \rightarrow s'
$$

$\Psi$, being a different class of object, naturally exposes different methods.
in the act of constructing a superposition of a letter, the action $\Psi.f$ is created by reflection on letter.
when $\Psi.f$ is called, it collapses the superposition (minimally).

in this way, superpositions re-enter the game logic as first-class objects.
other things may be superpositions and other methods may collapse them, for full nimrod procedural generation.

the $\Psi.f$ action is both an imperative fulfillment, and a player interaction. 

the player may still read the letter even when the imperative is not actively about providing information.
in this case, the superposition collapses minimally, destroying $\Psi.f$ and therefore destroying the imperative fulfillment.

the player may read the letter when the imperative is about providing information.
in this case, the superposition collapses to a state driven by the imperative, destroying $\Psi.f$ and the imperative fulfilment.

## actions as fundamental
the fundamental objects are actions.

* actions may be attached to superpositions or to objects
* actions may be triggered by the player or by the director
* actions on superpositions may collapse the superposition
* actions may fulfill imperatives
* actions may collapse a superposition in a motivated way to fulfill an imperative

$$
f_1 : () \rightarrow s'
\\
f_2 : i \rightarrow s'
\\
f_3 : p \rightarrow s'
\\
f_4 : (p, i) \rightarrow s'
$$

object letter exposes an action

$$l.f : p \rightarrow s.display(l.c)$$

this action (read) requires player interaction, and it displays the letter contents.

suppose we have imperative $i$ and that the player interacting with $l.f$ will fulfill the imperative. 
then we have

$$l.f : (p, i) \rightarrow s.display(l.c)$$

where $s.display$ fulfills the imperative.

now put the letter in a superposition:

$$
\Psi: {l}
\\
\Psi.f: p \rightarrow \psi.f(p)
$$

the player can interact with (read) the superposition, and the superposition collapses to $\psi$.

return to superposition and now introduce the imperative, $i$.

$$
\Psi: {l}
\\
\Psi.f: (p, i) \rightarrow \psi_i.f(p)
$$

now, when $\Psi$ collapses, it collapses to $\psi_i$ such that $\psi_i.f$ fulfills imperative $i$.

we need language to express the fact that $\Psi$ changes, and that $i$ is fulfilled.

---

in constructing $\Psi.f$ from $l.f$, we had to use the signature of $l.f$ to determine that 

---

**note**: the possible objects are still more general than the specifics of the plot.
like the imperative being more general than the plot.

state + imperative + collapse (player action) -> motivated collapse
state + imperative + director action -> motivated random effect or outcome

writing does not map to speech, both writing and speech map to a third system.
someone who cannot hear / never learned to speak the language can learn to read it.



q2: how to motivate someone saying "i left the package in the drawer"


---

a depth-2 search from top level imperative would reveal this, or a depth-2 search from chest.inspect.

problem: collapse naturally handles the notion of historical / logical consistency.



new thoughts: objects exposing multiple methods of the sort
"news broadcast"
"personal letter"
"receive item"

and imperatives having multiple slots for achievements via news broadcast, personal letter

imperative knows how to adapt its specific content to the various interfaces.

concrete example:

imperative: player learns of kidnapping
adapts: news broadcast, personal letter
    news: "{person} has been reported missing today...."
    letter: "send us money or you'll never see {person} again"

object: letter
adapts: news broadcast, personal letter
    news broadcast: the envelope contains a newspaper clipping. the paper reads:
    letter: the envelope contains a letter made of cut out letters. the letter reads:

so there are interfaces on both sides, and a successful imperative connects up the two

the envelope contains a newspaper clipping. the paper reads:
"{person} has been reported missing today...."

now, if there is no 1-st level plug connection for the imperative interface, the director moves toward the right interface. this recovers the desired generality.
e.g. if there isn't a letter in the scene:

* mail slot
    * adapts: create letter

* window
    * adapts: brick tossed through with letter

* chest of drawers
    * adapts: contains object

so building out the graph, we desire an node that exposes one of the desired interfaces: news broadcast, personal letter

so from state, we can do

$$
state \rightarrow mail.createLetter \rightarrow letter.note \\
state \rightarrow mail.createLetter \rightarrow letter.news \\
state \rightarrow window.brick \rightarrow letter.note \\
state \rightarrow window.brick \rightarrow letter.news \\
state \rightarrow drawers.item(letter) \rightarrow letter.news \\
state \rightarrow drawers.item(letter) \rightarrow letter.note \\
$$

the real trick is in $\{state \rightarrow drawers.item(letter)\}$ because drawers.item could potentially create any item. somehow not only the interface but its result need to be managed. this is where the superposition idea came from: it handles it naturally.

we can represent all of this as either superpositions or a very wide directed graph (or both? equivalent?)

the idea is to expand the graph of possibilities starting from state. any exposed free action (mail slot letter, window brick) or the various outcomes of a free action (chest contains candle, chest contains gun, chest contains letter) are edges that take you to a new state, which specifies further edges.

in this sense, something like chest.item is more like a set of free actions intermediate following a player choice (look in chest).
or collapse $\{look(chest) \rightarrow chest.item(letter)\}$ to a single edge?

imperative knows how to fulfill itself if given certain actions: news, letter, clue