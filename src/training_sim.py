"""Training skill simulation: stack rank per day for every Training level.

Every day (in the game's order):
  1. Training gives the stack  number * MAX_EXP / DIVISOR[level]  experience, capped at the top
     of the level's rank cap.
  2. New creatures join without experience (the stack experience is shared by all of them).
  3. The rank of the grown stack is the rank at the end of the day.

Run:  python src/training_sim.py      (needs matplotlib: python -m pip install matplotlib)
The chart is shown and saved as src/training_sim.png.
"""
import os

import matplotlib.pyplot as plt

# ---------------------------------------------------------------- settings (edit these)
CREATURE = 'Imp'
MAX_EXP = 29750          # red text at the bottom of the stack experience window ("... out of 56000 exp")
RANK10_EXP = 17500       # experience needed for rank 10 (Ace, "100%" in the window)

START_NUMBER = 37        # creatures in the stack on day 1
GROWTH_PCT = 4           # daily growth: floor(number * 4%) new creatures (0 for stacks below 25)
GROWTH_EVERY_DAYS = 1    # 1 = every day, 7 = once a week

DAYS = 30


# Rank thresholds in % of RANK10_EXP (rank 1 .. rank 10)
RANK_PCT = [5, 11, 18, 26, 35, 45, 57, 69, 84, 100]

# Training levels: name, daily experience = MAX_EXP / divisor per creature, rank cap
LEVELS = [
    ('Basic',       33, 3),
    ('Advanced',    29, 5),
    ('Expert',      25, 7),
    ('Master',      20, 8),
    ('Grandmaster', 17, 10),
]


# ---------------------------------------------------------------- model
def rank_of(exp_per_creature):
    rank = 0
    for r, pct in enumerate(RANK_PCT, start=1):
        if exp_per_creature >= RANK10_EXP * pct / 100:
            rank = r
    return rank


def cap_exp(cap_rank):
    """Highest experience per creature that is still inside the cap rank."""
    if cap_rank >= 10:
        return MAX_EXP
    return RANK10_EXP * RANK_PCT[cap_rank] / 100 - 1


def simulate(divisor, cap_rank):
    """Experience per creature at the START of every day (before that day's training)."""
    number = START_NUMBER
    total = 0.0                      # experience of the whole stack
    days, exps, numbers = [], [], []
    for day in range(1, DAYS + 1):
        days.append(day)
        exps.append(total / number)
        numbers.append(number)

        # 1. training (start of the owner's turn), capped at the top of the cap rank
        total += number * MAX_EXP / divisor
        total = min(total, number * cap_exp(cap_rank))

        # 2. new creatures join without experience: the stack experience is shared by all of them
        if day % GROWTH_EVERY_DAYS == 0:
            number += number * GROWTH_PCT // 100
    return days, exps, numbers


def first_cap_day(days, exps, cap_rank):
    """First day that starts with the stack at the cap rank (None if never)."""
    for day, exp in zip(days, exps):
        if rank_of(exp) >= cap_rank:
            return day, exp
    return None


# ---------------------------------------------------------------- chart
COLORS = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
STYLES = ['-', '--', '-.', ':', (0, (5, 1, 1, 1))]
MARKERS = ['o', 's', '^', 'D', 'v']


def draw_rank_lines(ax, labels=True):
    for r, pct in enumerate(RANK_PCT, start=1):
        y = RANK10_EXP * pct / 100
        ax.axhline(y, color='gray', linewidth=0.6, alpha=0.6)
        if labels:
            ax.text(1.002, y, ' R%d' % r, fontsize=7, va='center', transform=ax.get_yaxis_transform())
    ax.axhline(MAX_EXP, color='black', linewidth=0.6, alpha=0.4, linestyle='--')


def main():
    fig, axes = plt.subplots(3, 2, figsize=(13, 13))
    fig.suptitle('Training: %s (max exp %d, rank 10 at %d), start %d, +%d%% every %d day(s)\n'
                 'experience per creature at the start of each day, black circles = first day at every rank up to the cap'
                 % (CREATURE, MAX_EXP, RANK10_EXP, START_NUMBER, GROWTH_PCT, GROWTH_EVERY_DAYS))
    combined = axes[2][1]

    for i, (name, divisor, cap) in enumerate(LEVELS):
        days, exps, numbers = simulate(divisor, cap)
        hit = first_cap_day(days, exps, cap)

        ax = axes[i // 2][i % 2]
        ax.plot(days, exps, color=COLORS[i], marker=MARKERS[i], markersize=3)
        # milestones: every rank up to the cap rank of this level (labels alternate left / right)
        milestones = []
        for rank in range(1, cap + 1):
            reached = first_cap_day(days, exps, rank)
            if reached:
                milestones.append('R%d: day %d' % (rank, reached[0]))
                ax.plot([reached[0]], [reached[1]], 'o', markersize=9, markerfacecolor='none',
                        markeredgecolor='black', markeredgewidth=1.6)
                left = rank % 2 == 1
                ax.annotate('R%d: day %d' % (rank, reached[0]), reached, textcoords='offset points',
                            xytext=(-8, 4) if left else (8, -10), ha='right' if left else 'left', fontsize=7)
            else:
                milestones.append('R%d: never' % rank)
        draw_rank_lines(ax)
        ax.set_title('%s: 1/%d of max exp per day, cap rank %d' % (name, divisor, cap))
        ax.set_xlabel('day')
        ax.set_ylabel('exp per creature')
        ax.grid(True, alpha=0.2)

        combined.plot(days, exps, color=COLORS[i], linestyle=STYLES[i], linewidth=1.8, label=name)
        if hit:
            combined.plot([hit[0]], [hit[1]], 'o', markersize=9, markerfacecolor='none',
                          markeredgecolor='black', markeredgewidth=1.5)

        print('%-12s %s  (%d creatures on day %d)' % (name, ', '.join(milestones), numbers[-1], DAYS))

    draw_rank_lines(combined)
    combined.set_title('All levels')
    combined.set_xlabel('day')
    combined.set_ylabel('exp per creature')
    combined.grid(True, alpha=0.2)
    combined.legend(loc='upper left', fontsize=8)

    fig.tight_layout()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'training_sim.png')
    fig.savefig(out, dpi=100)
    print('saved', out)
    plt.show()


if __name__ == '__main__':
    main()
