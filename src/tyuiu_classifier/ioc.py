from dishka import (
    Provider,
    provide,
    Scope,
    make_async_container
)

from .classifier import BinaryClassifier
from .constants import (
    LABEL_BINARIZER_PATH,
    LABEL_ENCODER_PATH,
    ONE_HOT_ENCODER_PATH,
    STANDARD_SCALER_PATH,
    CLASSIFIER_PATH
)
from .estimators import (
    LabelBinarizer,
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    Classifier
)


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def get_label_binarizer(self) -> LabelBinarizer:
        return LabelBinarizer(LABEL_BINARIZER_PATH)

    @provide(scope=Scope.APP)
    def get_label_encoder(self) -> LabelEncoder:
        return LabelEncoder(LABEL_ENCODER_PATH)

    @provide(scope=Scope.APP)
    def get_one_hot_encoder(self) -> OneHotEncoder:
        return OneHotEncoder(ONE_HOT_ENCODER_PATH)

    @provide(scope=Scope.APP)
    def get_standard_scaler(self) -> StandardScaler:
        return StandardScaler(STANDARD_SCALER_PATH)

    @provide(scope=Scope.APP)
    def get_classifier(self) -> Classifier:
        return Classifier(CLASSIFIER_PATH)

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


container = make_async_container(AppProvider())
