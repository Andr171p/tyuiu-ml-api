from sklearn.pipeline import Pipeline


class BasePipelineFactory:
    def create_pipeline(self) -> "Pipeline":
        steps = [(name, step) for name, step in self.__dict__.items()]
        return Pipeline(steps)
