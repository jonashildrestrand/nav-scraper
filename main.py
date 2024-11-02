import scrape
import process
import argparse

def main():
    parser = argparse.ArgumentParser(description="verbose option")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()
    verbose = args.verbose

    if verbose:
        print("Verbose mode is enabled. Showing detailed output...")
    else:
        print("Verbose mode is disabled. Showing standard output.")

    # Scrape files from NAV
    SCRAPE_PATH = "./scraped/"
    scrape.download(SCRAPE_PATH, verbose)

    # Process scraped files
    process.filesInPath(SCRAPE_PATH, verbose)

if __name__ == "__main__":
    main()
