#! /bin/sh

FRAMES=300

python generator.py | python pypovswarm.py > out.pov
povray +D +R5 +J1.0 +KFF${FRAMES} +KC Display=on +Q8 +A0.5 +H720 +W1280 out.pov
