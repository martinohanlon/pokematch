Poke-Match
==========

Poke-Match is a simple but infuriating game. Match the Pokemon on the right with one on the left.

|pokematch|

Install
-------

Poke-Match uses guizero_ which can be installed using ``pip``.

Raspberry Pi / Linux::

    sudo pip3 install guizero

Windows::

    pip3 install guizero

MacOS also requires ``pillow``, due to it being unable to open PNGs::

    pip3 install guizero pillow

Clone the pokematch repository::

    git clone https://github.com/martinohanlon/pokematch

Run
---

Raspberry Pi / MacOS / Linux ::

    cd pokematch
    python3 pokematch.py

Windows ::

    cd pokematch
    python pokematch.py

Sprites
-------

The sprites were obtained from  https://github.com/PokeAPI/sprites

.. _guizero: https://lawsie.github.io/guizero

.. |pokematch| image:: pokematch.png

Problems
--------

It looks awful on the Mac because TkInter on the Mac doesnt support PNG or transparency, so they have to be converted to GIFs on the fly.