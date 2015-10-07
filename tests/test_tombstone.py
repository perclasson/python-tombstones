from tombstones import tombstone

def test(f):
    return f

@tombstone
def dead_code():
    pass


@tombstone
class ExampleClass:
    def test(self):
        pass


@tombstone
class SecondClass:
    class Test:
        @test
        @tombstone
        def not_used(self):
            pass

        def used(self):
            pass

SecondClass().Test().not_used()

dead_code()