import pytest

from apps.triage.domain.problem_record import PainType, ProblemRecord, Route, decide_route


def record(**kw) -> ProblemRecord:
    return ProblemRecord(confirmed=True, confidence=0.9, **kw)


def test_requires_confirmation():
    with pytest.raises(ValueError):
        decide_route(ProblemRecord(confirmed=False))


def test_acquisition_goes_to_build():
    assert decide_route(record(pain_type=PainType.ACQUISITION)).route is Route.BUILD


def test_operations_goes_to_solve_with_human():
    decision = decide_route(record(pain_type=PainType.OPERATIONS, processes_involved=1))
    assert decision.route is Route.SOLVE and decision.needs_human


def test_low_confidence_escalates():
    decision = decide_route(
        ProblemRecord(confirmed=True, confidence=0.3, pain_type=PainType.ACQUISITION)
    )
    assert decision.route is Route.OTHER and decision.needs_human


def test_out_of_scope():
    assert decide_route(record(out_of_scope=True)).route is Route.OTHER
