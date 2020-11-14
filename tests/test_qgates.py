
import qgates
from qgates import states, gates, qfn

def test_state_tensor():
    assert (qfn.tens(
        states.QB0,
        states.QB0
    ) == states.QB00).all()
    assert (qfn.tens(
        states.QB1,
        states.QB0
    ) == states.QB10).all()
    assert (qfn.tens(
        states.QB0,
        states.QB1
    ) == states.QB01).all()
    assert (qfn.tens(
        states.QB1,
        states.QB1
    ) == states.QB11).all()

def test_matmul():
    assert (qfn.matmul(
        gates.HAD,
        gates.HAD,
        states.QB0
    ).round(16).astype("int") == states.QB0).all()
    assert (qfn.matmul(
        gates.NOT,
        states.QB0
    ) == states.QB1).all()
