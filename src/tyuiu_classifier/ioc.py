from dishka import (
    Provider,
    provide,
    Scope,
    from_context,
    make_async_container
)

from .settings import Settings
from .classifier import BinaryClassifier
from .estimators import (
    LabelBinarizer,
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    Classifier
)


class AppProvider(Provider):
    config = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_label_binarizer(self, config: Settings) -> LabelBinarizer:
        return LabelBinarizer(config.LABEL_BINARIZER_PATH)

    @provide(scope=Scope.APP)
    def get_label_encoder(self, config: Settings) -> LabelEncoder:
        return LabelEncoder(config.LABEL_ENCODER_PATH)

    @provide(scope=Scope.APP)
    def get_one_hot_encoder(self, config: Settings) -> OneHotEncoder:
        return OneHotEncoder(config.ONE_HOT_ENCODER_PATH)

    @provide(scope=Scope.APP)
    def get_standard_scaler(self, config: Settings) -> StandardScaler:
        return StandardScaler(config.STANDARD_SCALER_PATH)

    @provide(scope=Scope.APP)
    def get_classifier(self, config: Settings) -> Classifier:
        return Classifier(config.CLASSIFIER_PATH)

    @provide(scope=Scope.APP)
    def get_binary_classifier(
            self,
            label_binarizer: LabelBinarizer,
            label_encoder: LabelEncoder,
            one_hot_encoder: OneHotEncoder,
            standard_scaler: StandardScaler,
            classifier: Classifier
    ) -> BinaryClassifier:
        return BinaryClassifier(
            label_binarizer=label_binarizer,
            label_encoder=label_encoder,
            one_hot_encoder=one_hot_encoder,
            standard_scaler=standard_scaler,
            classifier=classifier
        )


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
