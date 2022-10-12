#!/bin/bash
for lang in es fa fr it pl pt_BR tr; {
    python -m django makemessages -l $lang;
}
