def cool():
    def super_cool():
        return "I am very cool!"
    return super_cool


func = cool()

print(
    func,
    func()
)