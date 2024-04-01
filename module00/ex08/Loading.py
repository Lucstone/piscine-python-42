def ft_tqdm(lst: range) -> None:
    """
So let’s create a function called ft_tqdm.
The function must copy the function tqdm with the yield operator.
Here’s how it should be prototyped
    """
    for i in lst:
        j = i + 1
        prct = (j / len(lst)) * 100
        update = f"{j}/{len(lst)}"
        bar = (
            f"[{'='*int((j/len(lst))*50)}>{' '*(50-int((j/len(lst))*50))}]"
        )
        print(f"\r{prct:.0f}%{bar} {update}", flush=True, end="")
        yield i


def main():
    return


if __name__ == "__main__":
    main()
