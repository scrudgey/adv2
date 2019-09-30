# collapse notes
## 9/28

the collapse is only ever determined just-in-time, but it collapses in such a way that consistency is maintained (never contradicts self) and certain things are conserved.
at the same time, collapse proceeds in a motivated way, to advance the general game state toward certain story goals.

issues to be determined:

1. just-in-time rendering
2. internal / historical consistency guarantee
3. motivated collapse

## 1. just-in-time rendering

the hope is that this problem is manageable while possibly defining the space within which the harder problems will be solved.

purpose: as part of the main loop, the scene is rendered and presented to the player. 
anything in a superposition of descriptions will be forced into a choice in order to present a single description to the player.

first rule: superpositions are never observed.

we call:

`room.observe() -> string (description)`

this must proceed as something like a recursive function. 
i imagine that it is calling `observe` on various sub-components.
but, the way this is handled is not intrinsic to superposed objects but is just the result of how the room calculates `observe` in terms of observing sub-components.

1. `room.observe()`: first, room description itself collapses to a concrete value if it is a superposition, otherwise it returns concrete description.

*side note: generalization of collapse / superposed object?*

2. result: "your apartment", "a parlor", "the street"

3. next, room must also append descriptions of all the objects in the scene. it has some list of contained objects (this is the nature of the room) to describe as well. room wants to compile a list of "you see here:"

*side note: container is a point that could be abstracted*

4. room calls `item.observe()` on each item it contains and appends to the description.

5. `item` observes, possibly in a similar manner if it shares abstraction with room. in any case, 

`item.observe() -> string (description)`

### summary

abstractions:

**Superposable  interface** :
1. `collapse()`
   1. remove superposition / make concrete

**Describable interface** : Superposable
1. `observe(): string`
   1. side effect: collapse
   2. provide description

**Container interface** : Superposable
1. `items: List<Describable>`
2. override `observe()` to include description of items
3. possibly provide more detailed logic to mask certain items from description.

a key tension comes into focus.

`Describable` is a subclass of `Superposable` and its `observe` method has collapse as a side effect.
It must first collapse, then take its concrete value and call `observe`.
This general pattern will repeat for any type of object with any type of action that forces collapse, which is pretty much any type of object.

So the hope is that we can abstract superposable in a nicer way. Something similar
to the python implementation: it is a set that exposes all the maximal subset of all of its contained items