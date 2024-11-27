#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

hyfetch() {
    local flag_code=$((RANDOM % 4))
    local flag
    case $flag_code in
        0) flag='lesbian' ;;
        1) flag='transgender' ;;
        2) flag='rainbow' ;;
        *) flag='genderfluid' ;;
    esac
    command hyfetch -p "$flag"
}

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
