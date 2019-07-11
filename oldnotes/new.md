# notes
## 7/1/2019

motivation: it feels like there should be a simple, generalized description of what i'm trying to accomplish.

the collapse is only ever determined just-in-time, but it collapses in such a way that consistency is maintained (never contradicts self) and certain things are conserved.
this is the basis of the notion for the game. everything should be in superposition until just-in-time, when the scene is rendered for the player. 
when a QM state collapses, it is purely random; 
when our state collapses, we can motivate its collapse to be in a certain direction that is determined by a director with a larger goal in mind.

observation happens when something must be rendered: the scene is observed (all objects
visible in scene, not inside or behind other objects)

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

## collapse vs. action:

look more closely at the "motivated collapse" of the note text.
player reads note $\rightarrow$ player observes note.text $\rightarrow$ collapser collapses note.text $\rightarrow$ note.text is the imperative information $\rightarrow$ displayInformation(note.text) $\rightarrow$ imperative satisfied.

Does the collapser collapse the note text?

$$ \widehat{O}\ note.text \rightarrow information $$




---

**note**: the possible objects are still more general than the specifics of the plot.
like the imperative being more general than the plot.

state + imperative + collapse (player action) -> motivated collapse
state + imperative + director action -> motivated random effect or outcome




q2: how to motivate someone saying "i left the package in the drawer"