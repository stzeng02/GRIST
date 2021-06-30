import itertools

import pytest


class TestAllCallbacks:
    @pytest.fixture
    def callbacks(self):
        """Return all callbacks"""
        import scripts.study_case.ID_12.skorch.callbacks

        callbacks = []
        for name in dir(skorch.callbacks):
            attr = getattr(skorch.callbacks, name)
            # pylint: disable=unidiomatic-typecheck
            if not type(attr) is type:
                continue
            if issubclass(attr, skorch.callbacks.Callback):
                callbacks.append(attr)
        return callbacks

    @pytest.fixture
    def base_cls(self):
        from scripts.study_case.ID_12.skorch.callbacks import Callback
        return Callback

    @pytest.fixture
    def on_x_methods(self):
        return [
            'on_train_begin',
            'on_train_end',
            'on_epoch_begin',
            'on_epoch_end',
            'on_batch_begin',
            'on_batch_end',
            'on_grad_computed',
        ]

    def test_on_x_methods_have_kwargs(self, callbacks, on_x_methods):
        import inspect
        for callback, method_name in itertools.product(
                callbacks, on_x_methods):
            method = getattr(callback, method_name)
            assert "kwargs" in inspect.signature(method).parameters

    def test_set_params_with_unknown_key_raises(self, base_cls):
        with pytest.raises(ValueError) as exc:
            base_cls().set_params(foo=123)

        # TODO: check error message more precisely, depending on what
        # the intended message shouldb e from sklearn side
        assert exc.value.args[0].startswith('Invalid parameter foo for')
