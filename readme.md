# Awesome Crossplane Providers

This project queries a set of [Awesome Crossplane Providers](providers.txt) and generates overview pages to browse:

* An interactive table: [muvaf.github.io/awesome-crossplane-providers](https://muvaf.github.io/awesome-crossplane-providers/)
* A markdown file: [released-providers.md](./released-providers.md)
* A CSV: [repo-stats-latest.csv](./reports/repo-stats-latest.csv)

## How

This project consists 3 steps which are more or less automated: 

### 1) Generate the list of providers

This is done via the command "`axpp provider-names`" where it queries Github with a set of pre-defined queries and patterns (see [providers.go](/providers/providers.go)) to generate an alphabetical orderd list of providers and saves them to [provider.txt](provider.txt). The queries are somewhat fuzzy and can include false hits. Therefor we ignore all repositories listed in [providers-ignored.txt](providers-ignored.txt). All additions to providers.txt should be verified.

### 1) Generate the list of providers that depend on Terrajet

```console
cd terrajet-dependents
pip3 install -r requirements.txt
python3 main.py
```

### 2) Update provider statistics

This is done via the command "`axpp provider-stats`" where it reads provider.txt and queries Github for current repository information and release information and http://doc.crds.dev for information about the Providers CRDs. This command generates all artefacts apart from the site. It currently runs daily via an Github action.

### 3) Generate site

As a last step we generate a simple React app from the folder [site](./site/).

```console
cd site
yarn install && yarn build
rm -rf ../docs && mkdir ../docs && cp -a build/* ../docs/
```

## Dev

see [Makefile](Makefile)