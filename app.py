from flask import Flask, render_template, request, make_response
from utils import build_site_audit, build_social_proof, clean_url

app = Flask(__name__, template_folder='.', static_folder='assets', static_url_path='/assets')


@app.route('/styles.css')
def styles():
    with open('styles.css', 'r', encoding='utf-8') as css_file:
        response = make_response(css_file.read())
        response.headers['Content-Type'] = 'text/css'
        return response


@app.route('/', methods=['GET', 'POST'])
def index():
    social_proof = build_social_proof()

    if request.method == 'POST':
        website_url = clean_url(request.form.get('website_url', ''))
        industry = request.form.get('industry', 'SaaS').strip() or 'SaaS'
        audit_mode = request.form.get('audit_mode', 'Launch Readiness').strip() or 'Launch Readiness'

        if not website_url:
            return render_template(
                'index.html',
                report=None,
                social_proof=social_proof,
                website_url='',
                industry=industry,
                audit_mode=audit_mode,
                error='Please enter a website URL or domain.'
            )

        report = build_site_audit(website_url, industry, audit_mode)

        return render_template(
            'index.html',
            report=report,
            social_proof=social_proof,
            website_url=website_url,
            industry=industry,
            audit_mode=audit_mode,
            error=None
        )

    return render_template(
        'index.html',
        report=None,
        social_proof=social_proof,
        website_url='',
        industry='SaaS',
        audit_mode='Launch Readiness',
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True)
