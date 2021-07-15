import DevAuto as DA

@DA.testcase
def TC():
    GL8900T = DA.Dut("GL8900T")
    GL5610T = DA.Dut("GL5610T")

    GL8900 = DA.Tester("GL8900")
    PC1 = DA.Tester("PC")
    PC2 = DA.Tester("PC")

    m = GL8900T.query("route")  # type: DA.map,
    if m["127.0.0.1"]["MAC"] == "01:02:03:04:05:06":
        PC1.act("Send", "ICMP", dut)
    else:
        PC1.act("Send", "TCP", dut)

    GL8900.setVer(str(1+1))

    while 1 == 1:
        pass


def main():
    pass