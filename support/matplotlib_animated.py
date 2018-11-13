import matplotlib.pyplot
import matplotlib.animation
from matplotlib import style
import GUITest_Support

style.use('bmh')

ani = None


def init(top, gui, *args, **kwargs):        # import the root window with the 'w'variable
  global w, top_level, root
  w = gui
  top_level = top
  root = top


def handle_close(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani.event_source.stop()
    w.GraphButton1.configure(state='normal')


def handle_close2(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton2.configure(state='normal')


def handle_close3(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton3.configure(state='normal')


def handle_close4(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton4.configure(state='normal')


def handle_close5(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton5.configure(state='normal')


def handle_close6(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton6.configure(state='normal')


def handle_close7(evt):                      # function executed when Figure window close event is activated
    print('close figure')
    # ani2.event_source.stop()
    w.GraphButton7.configure(state='normal')


def animate_ch1(i):                         # animation for channel 1 window

    if len(xs1) > 10:
        del xs1[0]
        del ys1[0]

    xs1.append(GUITest_Support.ch1)
    ys1.append(GUITest_Support.ch2)

    ax1.clear()
    ax1.set_title(w.Entry2.get() + ' ' + 'Graph')
    ax1.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax1.set_ylabel(w.Entry2.get() + ' ' + w.UnitTCombobox2.get())
    ax1.plot(xs1, ys1, 'r', linewidth=1, label='chn 1')


def animate_ch2(i):                         # animation for channel 1 window

    if len(xs2) > 10:
        del xs2[0]
        del ys2[0]

    xs2.append(GUITest_Support.ch1)
    ys2.append(GUITest_Support.ch3)

    ax2.clear()
    ax2.set_title(w.Entry3.get() + ' ' + 'Graph')
    ax2.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax2.set_ylabel(w.Entry3.get() + ' ' + w.UnitTCombobox3.get())
    ax2.plot(xs2, ys2, 'g', linewidth=1, label='chn 2')


def animate_ch3(i):                         # animation for channel 1 window

    if len(xs3) > 10:
        del xs3[0]
        del ys3[0]

    xs3.append(GUITest_Support.ch1)
    ys3.append(GUITest_Support.ch4)

    ax3.clear()
    ax3.set_title(w.Entry4.get() + ' ' + 'Graph')
    ax3.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax3.set_ylabel(w.Entry4.get() + ' ' + w.UnitTCombobox4.get())
    ax3.plot(xs3, ys3, 'b', linewidth=1, label='chn 3')


def animate_ch4(i):                         # animation for channel 1 window

    if len(xs4) > 10:
        del xs4[0]
        del ys4[0]

    xs4.append(GUITest_Support.ch1)
    ys4.append(GUITest_Support.ch5)

    ax4.clear()
    ax4.set_title(w.Entry5.get() + ' ' + 'Graph')
    ax4.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax4.set_ylabel(w.Entry5.get() + ' ' + w.UnitTCombobox5.get())
    ax4.plot(xs4, ys4, 'c', linewidth=1, label='chn 4')


def animate_ch5(i):                         # animation for channel 1 window

    if len(xs5) > 10:
        del xs5[0]
        del ys5[0]

    xs5.append(GUITest_Support.ch1)
    ys5.append(GUITest_Support.ch6)

    ax5.clear()
    ax5.set_title(w.Entry6.get() + ' ' + 'Graph')
    ax5.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax5.set_ylabel(w.Entry6.get() + ' ' + w.UnitTCombobox6.get())
    ax5.plot(xs5, ys5, 'y', linewidth=1, label='chn 5')


def animate_ch6(i):                         # animation for channel 1 window

    if len(xs6) > 10:
        del xs6[0]
        del ys6[0]

    xs6.append(GUITest_Support.ch1)
    ys6.append(GUITest_Support.ch7)

    ax6.clear()
    ax6.set_title(w.Entry7.get() + ' ' + 'Graph')
    ax6.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax6.set_ylabel(w.Entry7.get() + ' ' + w.UnitTCombobox7.get())
    ax6.plot(xs6, ys6, 'y', linewidth=1, label='chn 6')


def animate_ch7(i):                         # animation for channel 1 window

    if len(xs7) > 10:
        del xs7[0]
        del ys7[0]

    xs7.append(GUITest_Support.ch1)
    ys7.append(GUITest_Support.ch8)

    ax7.clear()
    ax7.set_title(w.Entry8.get() + ' ' + 'Graph')
    ax7.set_xlabel(w.Entry1.get() + ' ' + w.UnitTCombobox1.get())
    ax7.set_ylabel(w.Entry8.get() + ' ' + w.UnitTCombobox8.get())
    ax7.plot(xs7, ys7, 'y', linewidth=1, label='chn 7')


def graph_plot_ch1():
    global ani, ax1, xs1, ys1
    print('open graph')

    # Resets the list before graph:
    xs1 = []
    ys1 = []

    plt1 = matplotlib.pyplot
    animation1 = matplotlib.animation

    fig1 = plt1.figure(1)
    fig1.canvas.mpl_connect('close_event', handle_close)                     # attach the event to the closing figure

    ax1 = fig1.add_subplot(111)                                              # generates the axi for the subplot
    ani = animation1.FuncAnimation(fig1, animate_ch1, interval=1000)          # creates the animation
    plt1.show()


def graph_plot_ch2():
    global ani2, ax2, xs2, ys2, plt2
    print('open graph')

    # Resets the list before graph:
    xs2 = []
    ys2 = []

    plt2 = matplotlib.pyplot
    animation2 = matplotlib.animation

    fig2 = plt2.figure(2)
    fig2.canvas.mpl_connect('close_event', handle_close2)                     # attach the event to the closing figure

    ax2 = fig2.add_subplot(111)                                              # generates the axi for the subplot
    ani2 = animation2.FuncAnimation(fig2, animate_ch2, interval=1000)          # creates the animation

    plt2.show()


def graph_plot_ch3():
    global ani3, ax3, xs3, ys3, plt3
    print('open graph')

    # Resets the list before graph:
    xs3 = []
    ys3 = []

    plt3 = matplotlib.pyplot
    animation3 = matplotlib.animation

    fig3 = plt3.figure(3)
    fig3.canvas.mpl_connect('close_event', handle_close3)                     # attach the event to the closing figure

    ax3 = fig3.add_subplot(111)                                              # generates the axi for the subplot
    ani3 = animation3.FuncAnimation(fig3, animate_ch3, interval=1000)          # creates the animation

    plt3.show()


def graph_plot_ch4():
    global ani4, ax4, xs4, ys4, plt4
    print('open graph')

    # Resets the list before graph:
    xs4 = []
    ys4 = []

    plt4 = matplotlib.pyplot
    animation4 = matplotlib.animation

    fig4 = plt4.figure(4)
    fig4.canvas.mpl_connect('close_event', handle_close4)                     # attach the event to the closing figure

    ax4 = fig4.add_subplot(111)                                              # generates the axi for the subplot
    ani4 = animation4.FuncAnimation(fig4, animate_ch4, interval=1000)          # creates the animation

    plt4.show()


def graph_plot_ch5():
    global ani5, ax5, xs5, ys5, plt5
    print('open graph')

    # Resets the list before graph:
    xs5 = []
    ys5 = []

    plt5 = matplotlib.pyplot
    animation5 = matplotlib.animation

    fig5 = plt5.figure(5)
    fig5.canvas.mpl_connect('close_event', handle_close5)                     # attach the event to the closing figure

    ax5 = fig5.add_subplot(111)                                              # generates the axi for the subplot
    ani5 = animation5.FuncAnimation(fig5, animate_ch5, interval=1000)          # creates the animation

    plt5.show()


def graph_plot_ch6():
    global ani6, ax6, xs6, ys6, plt6
    print('open graph')

    # Resets the list before graph:
    xs6 = []
    ys6 = []

    plt6 = matplotlib.pyplot
    animation6 = matplotlib.animation

    fig6 = plt6.figure(6)
    fig6.canvas.mpl_connect('close_event', handle_close6)                     # attach the event to the closing figure

    ax6 = fig6.add_subplot(111)                                              # generates the axi for the subplot
    ani6 = animation6.FuncAnimation(fig6, animate_ch6, interval=1000)          # creates the animation

    plt6.show()


def graph_plot_ch7():
    global ani7, ax7, xs7, ys7, plt7
    print('open graph')

    # Resets the list before graph:
    xs7 = []
    ys7 = []

    plt7 = matplotlib.pyplot
    animation7 = matplotlib.animation

    fig7 = plt7.figure(7)
    fig7.canvas.mpl_connect('close_event', handle_close7)                     # attach the event to the closing figure

    ax7 = fig7.add_subplot(111)                                              # generates the axi for the subplot
    ani7 = animation7.FuncAnimation(fig7, animate_ch7, interval=1000)          # creates the animation

    plt7.show()
